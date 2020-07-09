def makeSandvich(*components):
    # need to cobvert toopl to list!
    components = list(components);
    if 'bread' not in components:
        components.append('bread');

    print('Your sandvich has:');
    for component in components:
        print('\t-' + component);

makeSandvich('bread' , 'cheese');
makeSandvich('cheese');
