import re
from typing import Any

from data_classes import DifyNode, DifyNodeEdge, FlowLine


class DifyDSLConvertor:
    @classmethod
    def convert_dsl(
        cls, data: dict[str:Any], direction: str, language_setting: str
    ) -> str:
        nodes, edges = cls.__parse_dsl(data, language_setting)
        flow_lines = cls.__build_flow_lines(nodes, edges)
        flowchart_content = cls.__build_flowchart(direction, flow_lines)

        return flowchart_content

    @classmethod
    def __parse_dsl(
        cls,
        data: dict[str:Any],
        language_setting: str,
    ) -> tuple[list[DifyNode], list[DifyNodeEdge]]:
        graph = data.get("workflow", {}).get("graph", {})
        nodes_raw = graph.get("nodes", [])
        edges_raw = graph.get("edges", [])

        nodes = [
            DifyNode(
                id=n["id"],
                title=n.get("data", {}).get("title", ""),
                type=n.get("data", {}).get("type", ""),
                desc=n.get("data", {}).get("desc", ""),
                language=language_setting,
            )
            for n in nodes_raw
        ]

        edges = [
            DifyNodeEdge(
                source=e["source"],
                target=e["target"],
            )
            for e in edges_raw
        ]

        return nodes, edges

    @classmethod
    def __build_flow_lines(
        cls, nodes: list[DifyNode], edges: list[DifyNodeEdge]
    ) -> list[FlowLine]:
        id_map = {}
        for idx, node in enumerate(nodes, start=1):
            id_map[node.id] = f"id{idx:02d}"

        node_dec_lines = []
        for node_id, flow_id in id_map.items():
            node = next((n for n in nodes if n.id == node_id), None)
            if node:
                label = f"{node.title}【{node.local_type}】（{node.desc}）"
                line = f'    {flow_id}["{label}"]'
                node_dec_lines.append(FlowLine(text=line))

        node_dec_lines.append(FlowLine(text=""))

        edge_lines = []
        for edge in edges:
            src = next((n for n in nodes if n.id == edge.source), None)
            tgt = next((n for n in nodes if n.id == edge.target), None)
            if src and tgt:
                src_id = id_map[src.id]
                tgt_id = id_map[tgt.id]
                src_label = f"{src.title}【{src.local_type}】"
                tgt_label = f"{tgt.title}【{tgt.local_type}】"
                line = f'    {src_id}["{src_label}"] --> {tgt_id}["{tgt_label}"]'
                edge_lines.append(FlowLine(text=line))

        def id_key(s: str) -> int:
            m = re.match(r"^id(\d+)", s.replace(" ", ""))
            return int(m.group(1)) if m else float("inf")

        sorted_edge_lines = sorted(edge_lines, key=lambda line: id_key(line.text))

        total_lines = node_dec_lines + sorted_edge_lines
        return total_lines

    @classmethod
    def __build_flowchart(cls, mode: str, flowchart_lines: list[FlowLine]) -> str:
        header = f"flowchart {mode}"
        body = "\n".join(line.text for line in flowchart_lines)
        return f"{header}\n{body}"
