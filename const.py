HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Mermaid Flowchart Render</title>
    <script type="module">
      import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
      mermaid.initialize({{ startOnLoad: true }});
    </script>
</head>
<body>
    <div class="mermaid">
        {flowchart_str}
    </div>
    <div>
        {html_content}
    </div>
</body>
</html>
"""
"""output html template"""

DIFY_NODE_TYPE_MAPPING_EN = {
    "start": "Start node",
    "end": "End node",
    "answer": "Answer node",
    "llm": "LLM node",
    "knowledge-retrieval": "Knowledge Retrieval node",
    "question-classifier": "Question Classifier node",
    "if-else": "IF/ELSE node",
    "code": "Code Execution node",
    "template-transform": "Template node",
    "http-request": "HTTP Request node",
    "variable-assigner": "Variable Assigner node",
    "variable-aggregator": "Variable Aggregator node",
    "assigner": "Variable Assigner node",
    "iteration-start": "Iteration Start node",
    "iteration": "Iteration node",
    "parameter-extractor": "Parameter Extraction node",
    "document-extractor": "Doc Extractor node",
    "list-operator": "List Operator node",
    "agent": "Agent node",
    "loop-start": "Loop Start node",
    "loop": "Loop node",
    "loop-end": "Loop End node",
    "tool": "Tool node",
}
"""Map of Dify types in English"""

DIFY_NODE_TYPE_MAPPING_ZH = {
    "start": "开始 节点",
    "end": "结束 节点",
    "answer": "直接回复 节点",
    "llm": "LLM 节点",
    "knowledge-retrieval": "知识检索 节点",
    "question-classifier": "问题分类 节点",
    "if-else": "条件分支 节点",
    "code": "代码执行 节点",
    "template-transform": "模板转换 节点",
    "http-request": "HTTP 请求 节点",
    "variable-assigner": "变量赋值 节点",
    "variable-aggregator": "变量聚合 节点",
    "assigner": "变量赋值 节点",
    "iteration-start": "迭代开始 节点",
    "iteration": "迭代 节点",
    "parameter-extractor": "参数提取 节点",
    "document-extractor": "文档提取器 节点",
    "list-operator": "列表操作 节点",
    "agent": "Agent 节点",
    "loop-start": "循环开始 节点",
    "loop": "循环 节点",
    "loop-end": "循环结束 节点",
    "tool": "工具 节点",
}
"""Dify节点的中文名辞典"""

DIFY_NODE_TYPE_MAPPING_JP = {
    "start": "開始 ノード",
    "end": "終了 ノード",
    "answer": "回答 ノード",
    "llm": "LLM ノード",
    "knowledge-retrieval": "知識検索 ノード",
    "question-classifier": "質問分類器 ノード",
    "if-else": "IF/ELSE ノード",
    "code": "コード実行 ノード",
    "template-transform": "テンプレート ノード",
    "http-request": "HTTP リクエスト ノード",
    "variable-assigner": "変数代入器 ノード",
    "variable-aggregator": "変数集約器 ノード",
    "assigner": "変数代入器 ノード",
    "iteration-start": "イテレーション開始 ノード",
    "iteration": "イテレーション ノード",
    "parameter-extractor": "パラメータ抽出 ノード",
    "document-extractor": "テキスト抽出 ノード",
    "list-operator": "リスト処理 ノード",
    "agent": "エージェント ノード",
    "loop-start": "ループ開始 ノード",
    "loop": "ループ ノード",
    "loop-end": "ループ完了 ノード",
    "tool": "ツール ノード",
}
"""Difyノードタイプを日本語にマッピングする辞書"""

LANGUAGE_MAPPING = {
    "en_US": DIFY_NODE_TYPE_MAPPING_EN,
    "zh_Hans": DIFY_NODE_TYPE_MAPPING_ZH,
    "ja_JP": DIFY_NODE_TYPE_MAPPING_JP,
}
"""Map of language and name of Dify nodes types"""
