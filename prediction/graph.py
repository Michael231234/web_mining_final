from sklearn.externals import joblib
import matplotlib.pyplot as plt


clf = joblib.load('J:\\PycharmProjects\\prediction\\decision_tree1.pkl')
importance = clf.tree_.compute_feature_importances(normalize=False)
features = []
for i in range(len(importance)):
    features.append('f%d:' % i)
    print('f%d:' % i, importance[i])

plt.bar(range(len(importance)), importance, color='blue', tick_label=features)
plt.show()
plt.savefig('feature_importance.png')

# f0: 0.02510216558142463
# f1: 0.02877617086535361
# f2: 0.010002678929104352
# f3: 0.011276957378343751
# f4: 0.014037539451817224
# f5: 0.018546747333665882
# f6: 0.0023054590822512064
# f7: 0.017017781035014147
# f8: 0.02011778736918766
# f9: 0.00237636318524581
# f10: 0.013530256746927722
# f11: 0.010858451072994588
# f12: 0.01176079654496021
# f13: 0.014924908655745108
# f14: 0.026229761635669705
# f15: 0.030746928619635478
# f16: 0.020131092280443044
# f17: 0.0070271510463894024
# f18: 0.008938128004623893
# f19: 0.3815343699664735

