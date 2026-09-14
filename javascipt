import java.util.HashMap;
import java.util.Map;

class Solution {
		public int[] twoSum(int[] nums, int target) {
				Map<Integer, Integer> indicesByValue = new HashMap<>();

				for (int index = 0; index < nums.length; index++) {
						int complement = target - nums[index];

						if (indicesByValue.containsKey(complement)) {
								return new int[] {indicesByValue.get(complement), index};
						}

						indicesByValue.put(nums[index], index);
				}

				return new int[0];
		}
}
