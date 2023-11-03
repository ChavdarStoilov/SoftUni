export default function TableItems(
    {
        _id,
        teskText,
        isCompleted,
        // ChangeStatusTask
    }
) {
    

    

    return (
      <tr className={isCompleted ? "todo is-completed" : 'todo'}>
        <td>{ teskText }</td>
        <td>{isCompleted ? 'Complete' : 'Incomplete'}</td>
        <td className="todo-action">
          {/* <button className="btn todo-btn" onClick={ChangeStatusTask(_id)}>Change status</button> */}
        </td>
      </tr>
  );
}
