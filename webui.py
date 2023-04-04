from passphrase import gen_words

def write_html(words, num_words):
    f = open('passphrase.html', 'w')
    html = "<html>\n<head>\n<title>Passphrase</title>\n<body>\n"

    # Generate page title
    title = "Thanks for using Passphrase! Use the following {} words in your passphrase:\n".format(num_words)
    html = html + "<h1>" + title + "</h1>\n<body>\n"

    # Generate body for page
    body = "<p>\n"
    for i in range(1,num_words + 1):
        body = body + "Word #{:<10}".format(str(i))
    body = body + "</p>\n<p>\n"

    for word in words:
        body = body + "{:<16}".format(word)

    html = html + body + "\n</p>"

    sendoff = "\n<h2>Be sure to add other alphanumeric characters and capitalization to your new passphrase. Safe travels!</h2>"

    html = html + sendoff + "\n</body>\n</html"
    f.write(html)
    f.close()

words, num_words = gen_words()
write_html(words, num_words)