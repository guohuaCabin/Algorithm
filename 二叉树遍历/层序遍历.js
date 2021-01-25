function TreeNode(val) {
    this.val = val;
    this.left = this.right = null;
}

var levelOrderBottom = function(root) {
    let result = [];//输出结果
    let queue = [];//队列
    queue.push(root);//进栈
    let node;
    while (queue.length > 0) {
        let count = queue.length;//每个层级下的结点
        let list = [];
        for(let i = 0; i < count; i++){
            node = queue.shift();//出栈
            list.push(node.val);
            if(node.left != null){
                queue.push(node.left);
            }
            if(node.right != null){
                queue.push(node.right);
            }
        }
        result.push(list);
    }
    return result;
};

let a = TreeNode(3);
a.left = TreeNode(9);
a.right = TreeNode(20);
a.right.left = TreeNode(15);
a.right.right = TreeNode(7);

console.log(levelOrderBottom(a));