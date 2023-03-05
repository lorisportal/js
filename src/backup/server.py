from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import NumberInput

from model import MoneyModel
from mesa.visualization.modules import CanvasGrid, ChartModule

NUMBER_OF_CELLS = 30
SIZE_OF_CANVAS_IN_PIXELS_X = 900
SIZE_OF_CANVAS_IN_PIXELS_Y = 900

simulation_params = {
    "number_agents": NumberInput(
        "Choose how many agents to include in the model", value=NUMBER_OF_CELLS
    ),
    "width": NUMBER_OF_CELLS,
    "height": NUMBER_OF_CELLS,
}


def agent_portrayal(agent):
    if agent.buried:
        portrayal = {
            "Shape": "circle",
            "Filled": "true",
            "Color": "white",
            "r": 0.01,
            "text": "",
            "Layer": 0,
            "text_color": "black",
        }
        return portrayal

    portrayal = {
        "Shape": "circle",
        "Filled": "true",
        "r": 0.5,
        "text": f"ID:{agent.unique_id} Type: {agent.type}",
        "text_color": "black",
    }

    if agent.health > 50:
        portrayal["Color"] = "green"
        portrayal["Layer"] = 1

    else:
        portrayal["Color"] = "red"
        portrayal["Layer"] = 2
        portrayal["r"] = 0.2

    if agent.type == 0:
        portrayal["r"] = 0.2

    elif agent.type == 1:
        portrayal["r"] = 0.4

    elif agent.type == 2:
        portrayal["r"] = 0.6

    elif agent.type == 3:
        portrayal["r"] = 0.9

    if agent.dead:
        portrayal["Shape"] = "rect"
        portrayal["w"] = 0.2
        portrayal["h"] = 0.2
        portrayal["Color"] = "black"
        portrayal["Layer"] = 1

    return portrayal


grid = CanvasGrid(
    agent_portrayal,
    NUMBER_OF_CELLS,
    NUMBER_OF_CELLS,
    SIZE_OF_CANVAS_IN_PIXELS_X,
    SIZE_OF_CANVAS_IN_PIXELS_Y,
)

chart_healthy = ChartModule(
    [
        {"Label": "Healthy Agents", "Color": "green"},
        {"Label": "Non Healthy Agents", "Color": "red"},
    ],
    canvas_height=300,
    data_collector_name="datacollector_currents",
)


server = ModularServer(
    MoneyModel,
    [grid, chart_healthy],
    "Money Model",
    simulation_params,
)
server.port = 8521  # The default
server.launch()
