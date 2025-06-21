from mcp.server.fastmcp import FastMCP
import requests

mcp = FastMCP("AMTB")

@mcp.resource("amtb://menu/{scope}", name="Menu")
def get_menu(scope: str = "amtb") -> str:
    """get menu dynamically from amtb.tw based on scope
       default scope will be amtb
    """
    response = requests.get(f'https://www.amtb.tw/v2/newcategory?scope={scope}')
    menu = response.json()
    return menu

@mcp.resource("amtb://menu/{scope}/{amtb_id}", name="Sub Menu")
def get_sub_menu(amtb_id: str, scope: str = "amtb") -> str:
    response = requests.get(f'https://www.amtb.tw/v2/newcategory/{amtb_id}')
    subitem_json = response.json()
    return subitem_json

if __name__ == "__main__":
    mcp.run(transport='stdio')
    #print(get_sub_menu("48"))
    #print(get_menu())
