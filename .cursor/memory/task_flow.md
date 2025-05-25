# Task Flow Management

## Active Sprint
### Current Iteration: [Sprint N]
- **Theme**: [本次迭代主题]
- **Velocity**: [预计速度]

## Task Pipeline
### 🔴 In Progress
- [ ] **[Task ID]**: [任务描述]
  - Complexity: [1-5]
  - Dependencies: [依赖]
  - Progress: [进度条]

### 🟡 Up Next
- [ ] **[Task ID]**: [任务描述]
  - Estimated: [预估时间]
  - Prerequisites: [前置条件]

### 🟢 Completed
- [x] **[Task ID]**: [任务描述]
  - Actual Time: [实际时间]
  - Learnings: [经验教训]

## Dependency Graph
```mermaid
graph TD
    A[Task 1] --> B[Task 2]
    A --> C[Task 3]
    B --> D[Task 4]