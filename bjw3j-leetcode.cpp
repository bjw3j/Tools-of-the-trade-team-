/*
*******************************************
Author: Buddy White
Computing ID:bjw3j
Date: 2/24/2021
title: sort two arrays
Description:

This program will accept any 2 arrays of any length (except zero)
and will compute the median between them.

Language: C++

*******************************************
*/

#include <algorithm>
#include <vector>
class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {

        int size = nums1.size()+nums2.size();//finds the size of the 2 arrays added so it knows where the middle is
        vector<int> nums3(size);

        merge(nums1.begin(),nums1.end(),nums2.begin(),nums2.end(),nums3.begin());//merges the two vectors together into one vector so that it can pefrom the median operations on it
        if(size == 2){//if size is too small the formula won't work so it needs to have a case for that
            return double((nums3[0]+nums3[1])/double(2));//simpily divides the first and second element
        }

        else if(size == 1){//if size is one it will return just one number
            return double(nums3[0]);
        }

        else if(size%2==0){//with even sizes it will need to take an average of the two middle terms
            return double((nums3[(size/2)-1]+nums3[(size/2)])/double(2));
        }
        else{//if the size is just odd and not 2 or 1 then it does the normal median operation on it
            return double(nums3[size/2]);

        }

    }
};
