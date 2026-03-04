# MCP Server Example: CSV Search

## What is an MCP Server?

Just like your phone has apps that give it new abilities — maps, your calendar, a weather forecast — **MCP servers give Claude new abilities.**

Out of the box, Claude is a brilliant conversationalist, but it can only work with information you paste into the chat. An MCP server is a small plug-in that connects Claude to something external: a spreadsheet, a database, an internal system, an API. Once connected, Claude can reach in and pull real data.

**No more copying and pasting data into Claude.** It can look things up directly.

---

## What Does This MCP Server Do?

This server gives Claude two new abilities:

1. **Search a CSV file** — You can say "search my Q1 revenue file for Aetna" and Claude will scan the spreadsheet and return every matching row. It works on any column you specify.

2. **Summarize a CSV file** — You can say "what's in my contract tracker spreadsheet?" and Claude will tell you the row count, column names, and show you a few sample rows so you understand what you're working with.

Think of it as giving Claude the ability to query any spreadsheet like a database — without needing to open Excel or hire a data analyst for a simple lookup.

---

## How to Install It

Follow these steps in order. You only need to do this once.

**Step 1: Make sure Python is installed.**
Open your terminal (on a Mac, press Command + Space and type "Terminal") and type:
```
python3 --version
```
You should see something like `Python 3.11.4`. If you get an error, download Python from [python.org](https://python.org) and install it.

**Step 2: Navigate to this folder.**
In the same terminal window, type:
```
cd /Users/hammermt/Codes/every-headway-exec/examples/mcp-server
```
(Adjust the path if you saved this folder somewhere else.)

**Step 3: Install the required packages.**
```
pip install -r requirements.txt
```
This installs the MCP library and pandas (a tool for reading spreadsheets). It only takes a minute.

**Step 4: Open Claude Code in your project.**
Launch Claude Code as you normally would.

**Step 5: Register this MCP server with Claude.**
Run this command — replace `/full/path/to/server.py` with the actual path on your computer:
```
claude mcp add csv-search -- python3 /full/path/to/server.py
```
For example, if your file is at `/Users/jane/examples/mcp-server/server.py`, you would run:
```
claude mcp add csv-search -- python3 /Users/jane/examples/mcp-server/server.py
```

**Step 6: Restart Claude Code.**
Close and reopen Claude Code so it picks up the new server.

**Step 7: Try it out.**
Ask Claude things like:
- "Summarize the file /Users/jane/revenue.csv"
- "Search /Users/jane/contracts.csv in the Customer column for Aetna"
- "Look through my spreadsheet and find all rows where Region says Northeast"

Claude will use the MCP server to look through your actual files and return real results.

---

## How to Customize It

Every tool Claude gains from an MCP server is just a Python function in `server.py`. If you want to add a new ability, you add a new function.

For example, to add a tool that finds the top 5 largest values in a column, you would add a function like this to `server.py`:

```python
@mcp.tool()
def top_values(filename: str, column: str) -> str:
    """Return the 5 largest values in a column of a CSV file."""
    df = pd.read_csv(filename)
    top = df.nlargest(5, column)
    return top.to_string(index=False)
```

Each tool follows the same pattern:
- The `@mcp.tool()` line tells Claude this is an available tool
- The function name becomes the tool name
- The description in quotes tells Claude what the tool does and when to use it
- The rest is standard Python code

If your organization has a developer, they can connect these tools to live databases, internal APIs, your EHR system, or any data source your company uses — not just CSV files.

---

## Why This Matters

Most AI tools are disconnected from your actual work. They can answer general questions, but they don't know your patients, your contracts, your revenue numbers, or your operations.

MCP servers close that gap. When Claude is connected to your real data, it can help you:

- Find specific records in seconds instead of searching spreadsheets manually
- Summarize large datasets before diving into detail
- Answer questions like "how many claims came from Cigna last quarter?" directly from your files

The example here is intentionally simple — a CSV reader. But the same approach scales up: connect Claude to your CRM, your finance system, your scheduling software. Each connection is one more MCP server, and each one makes Claude more useful for your specific work.

**This is what turns Claude from a smart chatbot into a tool that understands your business.**
