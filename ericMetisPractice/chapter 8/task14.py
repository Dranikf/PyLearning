def make_car(maker , model , **eData):
    result = {  'maker' : maker,
                'model' : model,
                };
    for key, item in eData.items():
        result[key] = item;
    return result;
