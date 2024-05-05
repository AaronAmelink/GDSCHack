using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class gameManager : MonoBehaviour
{
    // Start is called before the first frame update
    public GameObject artPrefab;
    public roomScript startPlatform;
    public List<GameObject> doorways;
    public List<GameObject> openPaintingLocations;
    public List<GameObject> roomPrefabs;
    public GameObject doorwayBlocker;

    private void OnDrawGizmos()
    {
        Gizmos.color = Color.red;

        for (int j = 0; j < doorways.Count; j++)
        {
            Gizmos.DrawSphere(doorways[j].transform.position, 1);
            Ray ray = new Ray(new Vector3(doorways[j].transform.position.x, doorways[j].transform.position.y+10f, doorways[j].transform.position.z), Vector3.up *-1);
            Gizmos.DrawRay(ray);
        }
        
    }


    public void recieveJsonData(List<artPiece> pieces)
    {
        int numberOfPaintings = pieces.Count;
        startPlatform.doorways.ForEach(doorway =>
        {
            doorways.Add(doorway);
        });
        for (int i = 0; i < startPlatform.paintingAmount; i++)
        {
            openPaintingLocations.Add(startPlatform.paintingLocations[i]);
        }
        while (numberOfPaintings > openPaintingLocations.Count)
        {
            int whichDoor = Random.Range(0, doorways.Count);
            Debug.Log(whichDoor);
            GameObject newLocation = doorways[whichDoor];
            GameObject newObject = Instantiate(roomPrefabs[Random.Range(0, roomPrefabs.Count)]);
            newObject.transform.position = newLocation.transform.position;
            newObject.transform.rotation = newLocation.transform.rotation;
            roomScript newObjectRoomScript = newObject.GetComponent<roomScript>();
            for (int i = 0; i < newObjectRoomScript.paintingAmount; i++)
            {
                openPaintingLocations.Add(newObjectRoomScript.paintingLocations[i]);
            }
            for (int i = 0; i < newObjectRoomScript.doorways.Count; i++)
            {
                doorways.Add(newObjectRoomScript.doorways[i]);
            }

            doorways.Remove(newLocation);
        }

        for (int i = 0; i < pieces.Count; i++) 
        {
            GameObject newPiece = Instantiate(artPrefab);
            newPiece.GetComponent<artScript>().loadData(pieces[i].download, pieces[i].width, pieces[i].height, pieces[i].title, pieces[i].artist, pieces[i].created);
            int randomLocation = Random.Range(0, openPaintingLocations.Count);
            newPiece.transform.position = openPaintingLocations[randomLocation].transform.position;
            newPiece.transform.rotation = openPaintingLocations[randomLocation].transform.rotation;
            openPaintingLocations.RemoveAt(randomLocation);
        }

        for (int d  = 0; d < doorways.Count; d++)
        {
            GameObject blocker = Instantiate(doorwayBlocker);
            blocker.transform.position = doorways[d].transform.position;
            blocker.transform.rotation = doorways[d].transform.rotation;
        }



        
    }
}
