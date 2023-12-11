from langchain.chat_models.vertexai import ChatVertexAI
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
# from langchain.agents.agent_types import AgentType


def run(query, dataframe):
    agent = create_pandas_dataframe_agent(
        llm=ChatVertexAI(temperature=0.9, model_name="chat-bison", max_output_tokens=1000), df=dataframe, verbose=True)

    response = agent.run(query)

    return response
