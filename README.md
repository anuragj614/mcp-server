# MCP-Server

A Model Context Protocol (MCP) server that provides various tools for AI agents.

## Features

- **Web Search**: Perform web searches using Serper API.
- **Conversion Tools**: (Coming soon)

## Setup

1. **Install dependencies**:
   ```bash
   uv sync
   ```

2. **Configure Environment**:
   Copy the example environment file:
   ```bash
   cp .env.example .env
   ```
   Edit `.env` and add your API keys:
   - `SERPER_API_KEY`: Required for web search.

## Usage

### Running the Server
```bash
# Run the fastmcp server with docker
make dev

# Run the mcp client - MCP Inspector
make inspect
```

### Available Tools

#### `web_search`
Searches the web for a given query and returns organic search results including titles, links, and snippets.
- **Arguments**: `query` (str)
- **Returns**: List of search results.

## Development


- **Formatting**: `make format`
- **Type Checking**: `make mypy`

## Workflow

> [!IMPORTANT]
> All new feature branches should be branched out from the `dev` branch.