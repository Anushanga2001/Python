let arr = [20, 10, 5, 1];
arr.push(100);
arr.sort((a,b)=>(a-b));
console.log(arr);
console.log(arr[2]);

for (let i=5; i<=10; i++)
{
    console.log('*'.repeat(i));
}
for (let i=10; i>=5; i--)
{
        console.log('*'.repeat(i));
}

let i=5
while(i<=10)
{
    console.log('*'.repeat(i));
    i++;
}