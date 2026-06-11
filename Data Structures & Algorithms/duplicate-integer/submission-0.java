class Solution {
    public boolean hasDuplicate(int[] nums) {
        boolean containsDuplicate = false;
        for(int i = 0; i<nums.length;i++){
            for(int k = i+1; k<nums.length;k++){
                if(nums[i]==nums[k]){
                    containsDuplicate = true;
                }
            }
        }
        return containsDuplicate;
 
    }
}
