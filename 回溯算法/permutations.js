
function permutations(nums){
    let trackList = [];
    let resList = new Array();
    backTrack(nums,trackList,resList);
    return resList;
}

function backTrack(nums,trackList,resList){
    if (trackList.length == nums.length){
        resList.push(trackList.slice());
        return;
    }

    for(let i = 0; i < nums.length; i++){
        let select = nums[i];
        if(trackList.indexOf(select) > -1){
            continue;
        }
        trackList.push(select);
        backTrack(nums, trackList, resList);
        trackList.pop(select);
    }
}

let res = permutations([1,2,3])
for(let i = 0; i < res.length; i++){
    console.log(res[i]);
}
