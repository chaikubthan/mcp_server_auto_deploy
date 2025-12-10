from fastmcp import FastMCP

app = FastMCP()

@app.tool()
def hello(name: str) -> str:
    """
    Returns a greeting message.
    """
    return f"Hello, {name}! This is a FastMCP server from AWS via CI/CD."

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app.app, host="0.0.0.0", port=3000)
