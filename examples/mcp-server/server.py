# MCP Server: CSV Search
#
# This file turns Claude into a tool that can search through CSV files.
# Think of it as giving Claude the ability to act like a database query engine
# over any spreadsheet you point it to.
#
# How it works: FastMCP reads this file and exposes each @mcp.tool() function
# as a "tool" that Claude can call when you ask it questions.

from mcp.server.fastmcp import FastMCP
import pandas as pd

# Create the server and give it a name.
# This name is what Claude Code will display when showing available tools.
mcp = FastMCP("csv-search")


@mcp.tool()
def search_csv(filename: str, column: str, query: str) -> str:
    """
    Search a CSV file for rows where a specific column contains the query text.

    Args:
        filename: Full path to the CSV file (e.g. /Users/jane/revenue.csv)
        column:   The column name to search in (e.g. "Customer" or "Region")
        query:    The text to look for (e.g. "Aetna" or "Northeast")
    """
    df = pd.read_csv(filename)

    # Filter rows where the column value contains the search query (case-insensitive)
    mask = df[column].astype(str).str.contains(query, case=False, na=False)
    results = df[mask]

    if results.empty:
        return f"No rows found in '{column}' containing '{query}'."

    return f"Found {len(results)} matching rows:\n\n{results.to_string(index=False)}"


@mcp.tool()
def summarize_csv(filename: str) -> str:
    """
    Return a quick summary of a CSV file: row count, column names, and a few sample rows.

    Args:
        filename: Full path to the CSV file (e.g. /Users/jane/revenue.csv)
    """
    df = pd.read_csv(filename)

    summary = (
        f"File: {filename}\n"
        f"Rows: {len(df)}\n"
        f"Columns: {', '.join(df.columns.tolist())}\n\n"
        f"First 3 rows:\n{df.head(3).to_string(index=False)}"
    )
    return summary


# Start the server when this file is run directly.
if __name__ == "__main__":
    mcp.run()
