def compress(chars):
    output = []
    previous = None
    counter = 1
    for letter in chars:
        current = letter
        if current == previous:
            counter += 1
        elif current != previous and counter > 1:
            output.append(str(counter))
            counter = 1
            output.append(current)
        else:
            output.append(current)
        previous = current
    if counter > 1:
        output.append(str(counter))
    return output