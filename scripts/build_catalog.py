"""Render the reviewed catalog and verify its local navigation. No dependencies."""

import argparse
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def cell(value):
    text = str(value).replace("|", "&#124;").replace("\n", "<br>")
    # Google emits developer-site-relative links inside its descriptor text.
    return re.sub(r"\]\((/merchant/[^)]+)\)", r"](https://developers.google.com\1)", text)


def anchor(name):
    return re.sub(r"[^a-z0-9_-]", "-", name.lower())


def schema_type(schema):
    if "$ref" in schema:
        return schema["$ref"].split("/")[-1]
    if "anyOf" in schema or "oneOf" in schema:
        return " / ".join(schema_type(s) for s in schema.get("anyOf", schema.get("oneOf", [])))
    kind = schema.get("type", "any")
    if isinstance(kind, list):
        return " / ".join(kind)
    if kind == "array":
        return f"array of {schema_type(schema.get('items', {}))}"
    return kind


def parameter_table(schema):
    properties = schema.get("properties", {})
    if not properties:
        return ["No named parameters. See the exact schema below.", ""]
    lines = ["| Parameter | Type | Required | Default | Description |", "| --- | --- | --- | --- | --- |"]
    required = schema.get("required", [])
    for name, definition in properties.items():
        default = json.dumps(definition["default"], ensure_ascii=False) if "default" in definition else "—"
        description = definition.get("description", "")
        if "enum" in definition:
            description += " Allowed: " + ", ".join(json.dumps(x, ensure_ascii=False) for x in definition["enum"]) + "."
        lines.append(f"| `{cell(name)}` | {cell(schema_type(definition))} | {'Yes' if name in required else 'No'} | {cell(default)} | {cell(description) or '—'} |")
    return lines + [""]


def render_page(server, categories):
    tools = server["tools"]
    counts = Counter(t["operation"] for t in tools)
    lines = [f"# {server['title']}", "", "[Catalog](../../README.md) · [Find a tool](../../TOOLS.md) · "
             f"[Upstream]({server['upstream']}) · [Descriptors](../../catalog/{server['id']}.json)", "",
             server["summary"], "",
             f"**{len(tools)} tools:** " + ", ".join(f"{n} {k}" for k, n in sorted(counts.items())) + ". "
             f"**Reviewed:** {server['verifiedAt'][:10]}.", "",
             f"**Extraction:** {server['method']}", ""]
    if server.get("revision"):
        revision = server["revision"]
        if re.fullmatch(r"[0-9a-f]{40}", revision):
            lines += [f"**Source revision:** [{revision[:12]}]({server['upstream']}/tree/{revision}).", ""]
        else:
            lines += [f"**Source version:** {revision}.", ""]
    omitted = server["totalRegisteredTools"] - len(tools)
    completeness = f"All {len(tools)} Merchant Center and relevant setup tools are included"
    completeness += (f"; {omitted} unrelated tools from the {server['totalRegisteredTools']}-tool registry are omitted."
                     if omitted else ".")
    lines += [completeness, ""]
    if server.get("notes"):
        lines += ["## Implementation notes", ""]
        lines += [f"- {note}" for note in server["notes"]]
        lines += [""]
    lines += ["## Tools", "", "| Tool | Task | Effect |", "| --- | --- | --- |"]
    for tool in tools:
        lines.append(f"| [`{tool['name']}`](#{anchor(tool['name'])}) | {categories[tool['category']]['label']} | {tool['operation']} |")
    lines += [""]
    for tool in tools:
        description = tool["description"].strip() or "Upstream supplies no description."
        lines += [f"## {tool['name']}", ""]
        if tool.get("summary"):
            lines += [tool["summary"], ""]
        if description != tool.get("summary"):
            lines += ["<details>", "<summary>Full upstream description</summary>", "", "```text",
                      description, "```", "", "</details>", ""]
        lines += [f"**Effect:** {tool['operation']}. **Task:** {categories[tool['category']]['label']}. "
                  f"[Definition]({tool['source']}).", ""]
        if tool.get("availability"):
            lines += [f"**Availability:** {tool['availability']}", ""]
        lines += [f"**Note:** {note}" for note in tool.get("notes", [])]
        if tool.get("notes"):
            lines += [""]
        lines += parameter_table(tool["inputSchema"])
        lines += ["<details>", "<summary>Full parameter schema</summary>", "", "```json",
                  json.dumps(tool["inputSchema"], ensure_ascii=False, indent=2), "```", "", "</details>", ""]
    return "\n".join(lines)


def render_index(servers, categories):
    pairs = sorted(((t, s) for s in servers for t in s["tools"]), key=lambda p: (p[0]["name"].lower(), p[1]["id"]))
    lines = ["# Tool index", "", "[Catalog](README.md)", "",
             f"{len(pairs)} tool entries across {len(servers)} MCPs. Search this page for a tool name; each provider link opens its description and full parameters. Identical names from different providers have separate entries.", "",
             "**Effects:** read inspects data; write changes data or an approval ledger; setup changes authentication or registration; mixed combines reads with possible state changes.", "",
             "| Tool | Provider | Task | Effect |", "| --- | --- | --- | --- |"]
    for tool, server in pairs:
        href = f"docs/mcps/{server['id']}.md#{anchor(tool['name'])}"
        lines.append(f"| `{tool['name']}` | [{server['title']}]({href}) | {categories[tool['category']]['label']} | {tool['operation']} |")
    return "\n".join(lines) + "\n"


def render_main(servers, manifest):
    categories = manifest["categories"]
    total = sum(len(s["tools"]) for s in servers)
    latest = max(s["verifiedAt"][:10] for s in servers)
    lines = ["# Awesome Google Merchant Center MCP [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)", "",
             "> Find rejected products, inspect market prices, refresh feeds, and update catalog data through Merchant Center MCP tools.", "",
             f"**{len(servers)} MCPs · {total} tools** · [Search every tool](TOOLS.md). "
             "Each server has a reference page with descriptions and full input schemas.", "",
             "Merchant Center tools and their setup helpers are included; unrelated tools from multi-service servers are omitted. "
             "Groups follow the implemented tools, with each MCP listed once under its primary task.", "",
             f"**Latest source review:** {latest}, using runtime tool discovery and source inspection. "
             "No authenticated account operations were tested. Tool references distinguish reads, writes, setup, and mixed operations.", "",
             "## Contents", ""]
    populated = [(key, category, [s for s in servers if s["primaryCategory"] == key])
                 for key, category in categories.items()]
    populated = [item for item in populated if item[2]]
    for key, category, members in populated:
        lines.append(f"- [{category['label']} ({len(members)})](#{category['anchor']})")
    for key, companion in manifest["companions"].items():
        lines.append(f"- [{companion['title']} ({len(companion['entries'])})](#{key})")
    lines += [""]
    for key, category, members in populated:
        noun = "MCP" if len(members) == 1 else "MCPs"
        lines += [f"## {category['label']}", "", f"{len(members)} {noun}. {category['description']}", "",
                  "| MCP | What you can do | Tools |", "| --- | --- | --- |"]
        for server in members:
            href = f"docs/mcps/{server['id']}.md"
            examples = ", ".join(f"[`{name}`]({href}#{anchor(name)})" for name in server["examples"])
            lines.append(f"| [**{server['title']}**]({href}) | {server['summary']} Try {examples}. | [{len(server['tools'])}]({href}#tools) |")
        lines += [""]
    for companion in manifest["companions"].values():
        lines += [f"## {companion['title']}", "", f"{len(companion['entries'])} {companion['description']}", "",
                  "| Project | Merchant Center functionality |", "| --- | --- |"]
        for entry in companion["entries"]:
            lines.append(f"| [**{entry['name']}**]({entry['url']}) | {entry['description']} |")
        lines += [""]
    lines += ["[Contribute a tool](CONTRIBUTING.md).", ""]
    return "\n".join(lines)


def verify_schema_refs(schema):
    def walk(node):
        if isinstance(node, dict):
            ref = node.get("$ref")
            if ref and ref.startswith("#/"):
                target = schema
                for part in ref[2:].split("/"):
                    target = target[part.replace("~1", "/").replace("~0", "~")]
            for value in node.values():
                walk(value)
        elif isinstance(node, list):
            for value in node:
                walk(value)
    walk(schema)


def build():
    manifest = json.loads((ROOT / "catalog/manifest.json").read_text())
    categories = manifest["categories"]
    catalog_ids = {p.stem for p in (ROOT / "catalog").glob("*.json") if p.stem != "manifest"}
    assert catalog_ids == set(manifest["servers"]), "Catalog files and manifest disagree"
    assert len(manifest["servers"]) == len(set(manifest["servers"])), "Duplicate MCP in manifest"
    servers = [json.loads((ROOT / f"catalog/{slug}.json").read_text()) for slug in manifest["servers"]]
    outputs = {}
    for server in servers:
        assert server["id"] in manifest["servers"]
        assert server["primaryCategory"] in categories
        names = [t["name"] for t in server["tools"]]
        assert server["totalRegisteredTools"] >= len(names)
        assert len(names) == len(set(names)), f"Duplicate tools: {server['id']}"
        assert set(server["examples"]) <= set(names), f"Unknown example: {server['id']}"
        for tool in server["tools"]:
            assert tool["category"] in categories, (server["id"], tool["name"])
            assert tool["operation"] in ("read", "write", "setup", "mixed")
            assert tool["scope"] in ("merchant", "support")
            assert tool["source"].startswith("https://")
            assert isinstance(tool["inputSchema"], dict)
            verify_schema_refs(tool["inputSchema"])
        outputs[f"docs/mcps/{server['id']}.md"] = render_page(server, categories)
    outputs["TOOLS.md"] = render_index(servers, categories)
    outputs["README.md"] = render_main(servers, manifest)
    return outputs


def verify_links(outputs):
    for relative, content in outputs.items():
        # Schema examples and upstream descriptions can contain arbitrary Markdown.
        # Check the navigation we generate, rather than treating user-input examples as links.
        plain = re.sub(r"```.*?```", "", content, flags=re.S)
        for href in re.findall(r"\]\(([^\s)]+)\)", plain):
            if re.match(r"[a-z]+:", href):
                continue
            filename, _, fragment = href.partition("#")
            target = (ROOT / relative).parent / filename if filename else ROOT / relative
            target = target.resolve()
            assert target.is_relative_to(ROOT), f"Link escapes repo: {href}"
            target_relative = str(target.relative_to(ROOT))
            if target_relative in outputs:
                text = outputs[target_relative]
            else:
                assert target.is_file(), f"Broken link in {relative}: {href}"
                text = target.read_text()
            if fragment:
                headings = re.findall(r"^#{1,6} (.+)$", text, flags=re.M)
                anchors = {re.sub(r"[^\w -]", "", h.lower()).replace(" ", "-") for h in headings}
                assert fragment in anchors, f"Broken anchor in {relative}: {href}"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check snapshots and local links without writing")
    args = parser.parse_args()
    outputs = build()
    verify_links(outputs)
    stale = {str(p.relative_to(ROOT)) for p in (ROOT / "docs/mcps").glob("*.md")} - set(outputs)
    assert not stale, f"Remove obsolete generated MCP pages: {sorted(stale)}"
    for relative, content in outputs.items():
        target = ROOT / relative
        if args.check:
            assert target.is_file() and target.read_text() == content, f"Regenerate {relative}"
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content)
    print(f"{'Checked' if args.check else 'Generated'} {len(outputs)} pages; descriptors, source links, and local navigation are consistent.")


if __name__ == "__main__":
    main()
