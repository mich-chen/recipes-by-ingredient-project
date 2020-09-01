// ***** User's Food For Thoughts Component *****


function Tried(props) {
  let { id } = useParams();
  const {tried, setTried} = props;

  const handleTried = (e) => {
    const values = {
      true: 'True',
      false: 'False'
    };
    const triedValue = values[e.target.value];
    fetch('/api/user_thoughts', {
    method: 'POST',
    body: JSON.stringify({tried: triedValue, recipe_id: id}),
    headers: {'Content-Type': 'application/json'},
    credentials: 'include'
    })
    .then(res => res.json())
    .then(data => alert(data.message));
    if (e.target.value) {setTried(e.target.value)};
  };

  return (
    <div>
      <label> Tried recipe? </label>
      <Button id='yes-tried' variant='primary' value={true} onClick={handleTried} active={tried ? true : false}> yes </Button>
      <Button id='no-tried' variant='primary' value={false} onClick={handleTried} active={tried === false ? true : false}> no </Button>
    </div>
    );
}


function Comment(props) {
  let { id } = useParams();
  const {comment, setComment} = props;
  console.log(comment);

  const handleComment = () => {
    const newComment = document.getElementById('comment').value;
    fetch('/api/user_thoughts', {
    method: 'POST',
    body: JSON.stringify({comment: newComment, recipe_id: id}),
    headers: {'Content-Type': 'application/json'},
    credentials: 'include'
    })
    .then(res => res.json())
    .then(data => alert(data.message));
    setComment(newComment);
    document.getElementById('comment').value = ''
  };
  
  return (
    <div>
      <div>
        <Form.Label> Recipe Comment: </Form.Label>
        <p> {comment} </p>
        <FormControl id='comment' as="textarea"></FormControl>
        <Button variant='primary' type='submit' onClick={handleComment}>
          Save comment
        </Button>
      </div>
    </div>
    );
}


function FoodForThoughtsContainer(props) {
  let { id } = useParams();
  const [tried, setTried] = React.useState(null);
  const [rating, setRating] = React.useState(0);
  const [comment, setComment] = React.useState('');

  const [checked, setChecked] = React.useState(false);
  const [selected, setSelected] = React.useState([]);
  console.log('selected', selected);

  React.useEffect(() => {
    fetch(`/api/user_thoughts/${id}`)
    .then(res => res.json())
    .then(data => {
      console.log('data', data.thoughts);
      setTried(data.thoughts.tried);
      setRating(data.thoughts.rating);
      setComment(data.thoughts.comment);
    })
  },[]);

  return (
    <div>
      <Tried tried={tried} setTried={setTried} />

      <Comment comment={comment} setComment={setComment} />
    </div>
    );
}