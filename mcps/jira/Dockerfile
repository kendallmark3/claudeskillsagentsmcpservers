FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY server.py .

# MCP servers communicate over stdio by default.
# When running in Docker for team/cloud use, set MCP_TRANSPORT=sse
# and the FastMCP server will switch to HTTP SSE transport on $PORT.
ENV PORT=8000

CMD ["python", "server.py"]
