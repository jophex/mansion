# message = 'umetumiwa kisi cha tsh2000 kutoka kwa JOSEPH ALEX salio lako ni ths 9000 kujua bonyeza *148*99# ili ' \
#         'kujiunga na salio '
# if message.strip(".islower()"):
#   print(message)
# sentence = "XYThis is an example sentence.XY"
# print(message.strip(''))


number = input('enter dial codes')

if number == '*142*99#':
    print('Karibu Tigo Chagua kifurushi chako')

    li = ['Ofa Maalum', 'Zawadi kwa Rafiki', 'Dakika & SMS', 'Internet & 4G', 'Royal', 'Kimataifa', 'Kisichoisha Muda', 'Burudani', 'Tunashea Bando', 'Salio & Language']
    for i in range(len(li)):
        print(f'{i} {li[i]}')

choice = input('chagua kifurushi unachotaka')

while True:
    if choice == '0':
        print('your in one')

    elif choice == '1':
        print('your in 1')

    else:
        print('done')






else:
    print('wrong dial')
