using UnityEngine; using System.Collections; public class enemyMovement : MonoBehaviour
 { public Transform player; public Transform model; public Transform proxy; NavMeshAgent agent; NavMeshObstacle obstacle;
  void Start () 
  { agent = proxy.GetComponent< NavMeshAgent >(); obstacle = proxy.GetComponent< NavMeshObstacle >(); } 
  void Update () 
  { // Test if the distance between the agent (which is now the proxy) and the player 
  // is less than the attack range (or the stoppingDistance parameter) 
  if ((player.position - proxy.position).sqrMagnitude < Mathf.Pow(agent.stoppingDistance, 2)) 
  {
     // If the agent is in attack range, become an obstacle and 
     // disable the NavMeshAgent component 
     obstacle.enabled = true; agent.enabled = false; } else {
         // If we are not in range, become an agent again 
         obstacle.enabled = false; agent.enabled = true; 
         // And move to the player's position 
         agent.destination = player.position; }
          model.position = Vector3.Lerp(model.position, proxy.position, Time.deltaTime * 2); model.rotation = proxy.rotation; } }