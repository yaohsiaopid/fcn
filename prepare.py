for r in df.values:
...     im = cv2.imread(r[1])
...     out = np.zeros((im.shape[0], im.shape[1]))
...     out[r[3]:r[3]+r[5],r[2]:r[2]+r[4]] = 1
...     cv2.imwrite('label_%s.png' % r[1][:-4], out)
