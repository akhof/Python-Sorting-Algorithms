# Python-Sorting-Algorithms
In this project I implemented a few sorting algorithms in Python.
I also created a little comparison script to compare all these algorithm - you can find it's output bellow.

More details in my blog article (in german): https://arnehannappel.de/blog/28-sortieralgorithmen

## Algorithms
I implemented this algorithms: BadAlgorithm, BubbleSort, SelectionSort, InsertionSort, QuickSort, MergeSort and HeapSort

## Comparison script output
```
Elements          BadAlgorithm          BubbleSort          SelectionSort          InsertSort          HeapSort             MergeSort          QuickSort
2^2 = 4           0.0s (0.0%)           0.0s (0.0%)         0.0s (0.0%)            0.0010s (100.0%)    0.0s (0.0%)          0.0s (0.0%)        0.0s (0.0%)           
2^3 = 8           0.05715s (100.0%)     0.0s (0.0%)         0.0s (0.0%)            0.0s (0.0%)         0.0s (0.0%)          0.0s (0.0%)        0.0s (0.0%)           
2^4 = 16                                0.0s (0.0%)         0.0s (0.0%)            0.001s (100.0%)     0.0s (0.0%)          0.0s (0.0%)        0.0s (0.0%)           
2^5 = 32                                0.001s (100.0%)     0.001s (99.95%)        0.0s (0.0%)         0.00055s (54.78%)    0.00046s (45.55%)  0.00054s (53.99%)        
2^6 = 64                                0.00146s (97.32%)   0.0015s (100.0%)       0.0005s (33.35%)    0.0005s (33.32%)     0.0005s (33.35%)   0.0s (0.0%)           
2^7 = 128                               0.00652s (100.0%)   0.00504s (77.38%)      0.00401s (61.51%)   0.00301s (46.16%)    0.001s (15.37%)    0.001s (15.36%)        
2^8 = 256                               0.03208s (100.0%)   0.02807s (87.5%)       0.01153s (35.95%)   0.00351s (10.94%)    0.00255s (7.96%)   0.002s (6.23%)        
2^9 = 512                               0.10789s (100.0%)   0.07821s (72.49%)      0.04216s (39.07%)   0.00602s (5.58%)     0.00401s (3.72%)   0.00301s (2.79%)        
2^10 = 1024                             0.48238s (100.0%)   0.34102s (70.69%)      0.16595s (34.4%)    0.0211s (4.37%)      0.01404s (2.91%)   0.01203s (2.49%)        
2^11 = 2048                             1.69633s (100.0%)   1.25931s (74.24%)      0.66277s (39.07%)   0.03204s (1.89%)     0.02164s (1.28%)   0.01905s (1.12%)        
2^12 = 4096                             6.57889s (100.0%)   5.0763s (77.16%)       2.88635s (43.87%)   0.06969s (1.06%)     0.04763s (0.72%    0.03956s (0.6%)        
2^13 = 8192                                                 20.80974s (100.0%)     10.6925s (51.38%)   0.14694s (0.71%)     0.09521s (0.46%)   0.08026s (0.39%)        
2^14 = 16384                                                                       42.55045s (100.0%)  0.32948s (0.77%)     0.20857s (0.49%)   0.17949s (0.42%)        
2^15 = 32768                                                                                           0.72272s (100.0%)    0.46931s (64.94%)  0.40179s (55.59%)        
2^16 = 65536                                                                                           1.57748s (100.0%)    1.02373s (64.9%)   0.97124s (61.57%)        
2^17 = 131072                                                                                          3.71869s (100.0%)    2.35081s (63.22%)  1.73522s (46.66%)        
2^18 = 262144                                                                                          7.75541s (100.0%)    5.23734s (67.53%)  3.83925s (49.5%)        
2^19 = 524288                                                                                          17.55785s (100.0%)   11.3894s (64.87%)  8.33732s (47.48%)        
2^20 = 1048576                                                                                                              24.91203s (100.0%)   17.57118s (70.53%)        
2^21 = 2097152                                                                                                              53.311s (100.0%)     35.57808s (66.74%)        
2^22 = 4194304                                                                                                              116.41198s (100.0%)  81.92689s (70.38%)        
```