export default function TableItems(
    {
        teskText,
        isCompleted
    }
) {
    
    return (
      <tr className={isCompleted ? "todo is-completed" : 'todo'}>
        <td>{ teskText }</td>
        <td>{isCompleted ? 'Complete' : 'Incomplete'}</td>
        <td className="todo-action">
          <button className="btn todo-btn">Change status</button>
        </td>
      </tr>
  );
}
