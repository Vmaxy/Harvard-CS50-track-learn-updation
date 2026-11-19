def faces(texts):
    texts = (texts.replace(":)","🙂" ).replace(":(","🙁"))
    return texts

def main():
    print(faces(input()))
  
main()
