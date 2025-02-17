import openai
import click

openai.api_key = "YOUR_OPENAI_API_KEY"  # Вставь свой API-ключ OpenAI

@click.command()
@click.option('--repo', prompt="GitHub repository name", help="The name of your GitHub repo")
@click.option('--description', prompt="Short project description", help="A brief description of the project")
@click.option('--language', prompt="Programming language", help="Main language of the project")
def generate_readme(repo, description, language):
    """Generates a README.md file using AI"""
    prompt_text = f"Create a professional README.md file for a GitHub repository named '{repo}'. The project is a {language} application. Description: {description}."

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": prompt_text}]
    )

    readme_content = response["choices"][0]["message"]["content"]

    with open("README.md", "w") as file:
        file.write(readme_content)

    click.echo("✅ README.md successfully generated!")

if __name__ == '__main__':
    generate_readme()
