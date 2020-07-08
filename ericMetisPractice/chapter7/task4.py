
additinal_components = [];
message = 'input new component of the pizza or "ok" to finish program: '

while True:
    component = input(message);
    if component == 'ok':
        break;
    additinal_components.append(component);

print('\nyour complete is');
for component in additinal_components:
    print('\t' + component);
