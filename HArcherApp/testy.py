# punkty = '1 25--'
#
# arrows_shoot = 0
# missed_arrows = 0
# arrows_in_target_no_points = 0
# counted_arrows = 0
# result = 0
#
# for x in range(0,len(punkty)):
#
#     if punkty[x] == "-":
#         missed_arrows += 1
#         arrows_shoot += 1
#     elif punkty[x] == ' ':
#         print('')
#     elif punkty[x] == '0':
#         arrows_in_target_no_points += 1
#         arrows_shoot += 1
#     elif punkty[x] == '1' or punkty[x] == '2' or punkty[x] == '3' or punkty[x] == '4' or punkty[x] == '5':
#         counted_arrows += 1
#         result += int(punkty[x])
#         arrows_shoot += 1
#
# print(arrows_shoot)
# print(missed_arrows)
# print(arrows_in_target_no_points)
# print(counted_arrows)
# print(result)


# import matplotlib.pyplot as plt
# fig, ax = plt.subplots()
# ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
# [<matplotlib.lines.Line2D object at 0x0FBF5F58>]
# fig.show()