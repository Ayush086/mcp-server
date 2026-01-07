# MCP Server

## Setup Guide
```sh
pip install uv
```

```sh 
uv init .
```

```python
 uv add fastmcp
 ```
 NOTE: In similar way only other requirements must be installed **Not using 'pip install'**

 #### AFter completing the setup
 **to run the server**
 ```
 fastmcp run main.py --transport http --host 0.0.0.0 --port 8000
 ```

 **OR**

 ```
uv run main.py
 ```


#### Test the server in mcp inspector
```
uv run fastmcp dev main.py
```
- In left sidebar select the transport type to *streamable HTTP*
- Check the URL and click on *connect*
- Now we can inspect the mcp server from navigation bar
- *resources* tab can be used to see the resources, after clicking on *list resources*
- In *tool* we will be able to access the tools and use then in side window
