from langchain.llms.vertexai import VertexAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


def code(language, problem):
    llm = VertexAI(model_name="code-bison", max_output_tokens=1000)

    prompt_template = PromptTemplate(
        input_variables=['language', 'problem'], template="Write me a function in {language} to {problem}"
    )

    chain = LLMChain(llm=llm, prompt=prompt_template)

    response = chain({"language": language, "problem": problem})
    return response.get("text", "ERROR Occured!")


if __name__ == "__main__":
    with open("Output.txt", "w") as file:
        file.write(code(language="Python",
                   problem="Access secret value from Google Cloud Platform Secret Manager"))
        file.close()
