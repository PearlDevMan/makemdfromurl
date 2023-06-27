import openai
def getrewrite(filename):
    openai.api_key = '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'
    # Define the prompt and the original article
 
    path = "result//" + filename + ".txt"
    rewritten_article = ""
    # Call the OpenAI API to generate a rewritten version of the article
    with open(path, "r+") as f:
        article = f.read()
        prompt = f'''Rewrite(without yea or no) the following article by origin topics(started with #) and the content from following article 
        and don't add new topics, add related article from following article:\n\n{article}'''
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=1024,
            #n=1,
            #stop=None,
            temperature=0.7,
        )
        # Extract the rewritten article from the response
        rewritten_article = response.choices[0].text.strip()
        # Print the original and rewritten articles to the console
        f.write('\n\n REWRITED TEXT\n\n')
        f.write(rewritten_article)
    return rewritten_article