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
    // let newNums = nums.List.slice()
    for(let i = 0; i < nums.length; i++){
        let select = nums[i];
        if(trackList.indexOf(select) > -1){
            continue;
        }
        // nums.pop(select);
        trackList.push(select);
        backTrack(nums, trackList, resList);

        // newNums.push(select);
        trackList.pop(select);
    }
}
