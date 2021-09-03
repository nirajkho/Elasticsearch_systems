# Example data designed to match examples on slides
class ExampleData:
  actual = set(range(0,10*2,2))
  primary_example = [0,1,2,4,6,8,10,11,12,13,14,17,19,16,21,23,25,27,29,18]
  first_half_correct = range(0,10*2,2) + range(1,10*2,2)
  second_half_correct =  range(1,10*2,2) + range(0,10*2,2)
  swapped_2_3 = [0,2,1,4,6,8,10,11,12,13,14,17,19,16,21,23,25,27,29,18]
  swapped_8_9 = [0,1,2,4,6,8,10,12,11,13,14,17,19,16,21,23,25,27,29,18]

def rk(actual, predicted, k):
  # find all the matches from the ones we predicted
  matches = len(set(predicted[:k]) & set(actual))
  if matches == 0:
    return 0
  # what fraction of all the results did we find?
  return float(matches) / len(actual)

def pk(actual, predicted, k=10):
  """
  calculates P@K

  actual: the unordered set of correct answers
  predicted: the ordered list of predictions
  k: the k the precision is calculated at

  returns float
  """
  # get the first k predicted items
  k_predicted_items = set(predicted[:k])
  # the correct items
  actual = set(actual)
  # how many of those k predicted items are actual items?
  correct = len(k_predicted_items & actual)
  # precision - what fraction of the items is that?
  precision = correct/float(k)
  # return precision at k items
  return precision

def apk(actual, predicted, k=10):
  """
  calculates average precision

  actual: the unordered set of correct answers
  predicted: the ordered list of predictions
  k: the k the precision is calculated at

  returns float
  """
  actual = set(actual)
  k_predicted_items = predicted[:k]
  # find the PK for every one recall increases
  pks = [pk(actual, predicted, i+1) for i, p in enumerate(k_predicted_items) if p in actual]
  # return the average
  return sum(pks)/float(len(pks))

def mapk(actuals, predicteds):
  """
  Calculates MAP - Mean Average Precision
  actuals: are a list of lists (actual)
  predicteds: are a list of list (predicted)
  k: the k the precision is calculated at
  returns float
  """
  # find the APK of all the pairs of actual and predict results
  apks = ([apk (a, p, len (p)) for a, p in zip (actuals, predicteds)])
  # take the mean of that list
  return sum(apks) / float(len(apks))

COLOURS = {"END":'\033[0m',"RED":'\033[30;41m',"GREEN":'\033[30;42m'}
DISPLAY_CORRECT = {True: COLOURS["GREEN"], False: COLOURS["RED"]}

def pk_table(actual, predicted, k):
  print "Actual:", actual
  print "Predicted:", predicted
  print "{:^3} {:^7} {:^5} {:^5}".format("k", "Result", "R@k", "P@k")
  for k in range(1,min(k, len(predicted))+1):
    rounded_pk = round(pk(actual, predicted,k=k),2)
    rounded_rk = round(rk(actual, predicted,k=k),2)
    is_correct = predicted[k-1] in actual
    print "{:>3} {}{:^7}{} {:>5} {:>5}".format(k, DISPLAY_CORRECT[is_correct],predicted[k-1],COLOURS["END"], rounded_rk, rounded_pk)
  print "AP", round(apk(actual, predicted, k),2)

if __name__ == "__main__":
  sep = "-" * 70
  ex = ExampleData

  print sep
  print "Primary Example (Slide 43)"
  pk_table(ex.actual, ex.primary_example, 20)

  print sep
  print "First Half Correct (Slide 44)"
  pk_table(ex.actual, ex.first_half_correct, 20)

  print sep
  print "Second Half Correct - First Half Wrong (Slide 45)"
  pk_table(ex.actual, ex.second_half_correct, 20)

  print sep
  print "Swapped 2 & 3 (Slide 47)"
  pk_table(ex.actual, ex.swapped_2_3, 20)

  print sep
  print "Swapped 8 & 9 (Slide 49)"
  pk_table(ex.actual, ex.swapped_8_9, 20)
