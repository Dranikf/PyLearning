discClassik = {};

discClassik['jen'] = 'python'
discClassik['sarah'] = 'c'
discClassik['phil'] = 'python'
discClassik['edward'] = 'ruby'

for name, language in discClassik.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")
