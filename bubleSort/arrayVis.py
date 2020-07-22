def calcMode(array):

    length = len(array);

    width = length * 5;
    height = max(array) + 5;

    return (width, height);
