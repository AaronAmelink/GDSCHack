using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class gameManager : MonoBehaviour
{
    // Start is called before the first frame update
    public GameObject artPrefab;
    public float startPosition = 0;

    public void recieveJsonData(List<artPiece> pieces)
    {
        Debug.Log(pieces[15].title);
        for (int i = 0; i < pieces.Count; i++) 
        {
            startPosition += pieces[i].width*0.01f * 0.5f;
            GameObject newPiece = Instantiate(artPrefab);
            newPiece.GetComponent<artScript>().loadData(pieces[i].download, pieces[i].width, pieces[i].height, pieces[i].title, pieces[i].artist, pieces[i].created);
            newPiece.transform.position = new Vector3(startPosition,pieces[i].height *0.01f *0.5f + 0.5f, -5);
            startPosition += pieces[i].width * 0.01f * 0.5f;
        }
    }
}
