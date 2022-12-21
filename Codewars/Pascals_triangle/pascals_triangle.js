// https://www.codewars.com/kata/5226eb40316b56c8d500030f

function pascalsTriangle(n) {
  let result = [];
  let last_item;

  for (let i = 0; i < n; i++) {
    if (result.length == 0) {
      result.push([1]);
    } else if (result.length == 1) {
      result.push([1, 1]);
      last_item = [1, 1];
    } else {
      let temp_list = [];
      temp_list.push(1);

      for (let j = 0; j < last_item.length; j++) {
        if (j + 1 < last_item.length) {
          temp_list.push(last_item[j] + last_item[j + 1]);
        }
      }
      temp_list.push(1);
      result.push(temp_list);
      last_item = temp_list;
    }
  }

  let finalResult = [];
  result.forEach((item) => {
    finalResult = finalResult.concat(item);
  });
  return finalResult;
}
