### check cocoeval.py!

### cocoeval.py에 mAP 출력 코드 추가

'''

    import logging

          # line about 480에 추가
      else: 
          mean_s = np.mean(s[s>-1])

          # cacluate AP(average precision) for each category
          num_classes = len(p.catIds)
          # print(len(p.catIds))
          # print("check s.shape", s.shape)
          logger.info(f"p.catIds 갯수 = {len(p.catIds)}")
          logger.info(f"check s.shape: {s.shape}")

          avg_ap = 0.0
          if ap == 1:
              for i in range(0, num_classes):
                  print('category : {0} : {1}'.format(i, np.mean(s[:, :, i, :])))
                  logger.info('category : {0} : {1}'.format(i, np.mean(s[:, :, i, :])))
                  avg_ap += np.mean(s[:, :, i, :])
              print('(all categories) mAP : {}'.format(avg_ap / num_classes))
              logger.info('(all categories) mAP : {}'.format(avg_ap / num_classes))
          # assertEqual(p.catIds, 4)
      print(iStr.format(titleStr, typeStr, iouStr, areaRng, maxDets, mean_s))
      return mean_s
  
 
'''
