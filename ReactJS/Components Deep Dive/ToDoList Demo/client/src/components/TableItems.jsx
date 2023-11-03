export default function TableItems(
    {
        _id,
        teskText,
        isCompleted,
        onUpdate
    }
) {
    

    function UpdateTask() {
        onUpdate(_id, isCompleted);
    }
    return (
      <tr className={isCompleted ? "todo is-completed" : 'todo'}>
        <td>{ teskText }</td>
        <td>{isCompleted ? 'Complete' : 'Incomplete'}</td>
        <td className="todo-action">
        <button className="btn todo-btn" onClick={UpdateTask}>Change status</button>
        </td>
      </tr>
  );
}
