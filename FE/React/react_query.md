# React query 

## 基本使用

- 查询
  - useQuery
  - useQueryClient

```jsx
// 定义 query
function usePost(postId) {
  return useQuery({
    queryKey: ['post', postId],
    queryFn: () => getPostById(postId),
    enabled: !!postId,
})
// 查询 query
const queryClient = useQueryClient()
queryClient.getQueryData(['post', post.id])
```



## 重新获取

```jsx
  const { status, data, error, isFetching } = useQuery({
    queryKey: ['todos'],
    queryFn: async () => {
      const res = await axios.get('/api/data')
      return res.data
    },
    // 重新获取
    refetchInterval: intervalMs,
  })
```

## 分页

使用 `placeholderData`？？

无限滚动：

- react-intersection-observer
- useInfiniteQuery