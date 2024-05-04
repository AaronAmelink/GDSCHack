using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class gameManager : MonoBehaviour
{
    // Start is called before the first frame update
    public GameObject artPrefab;

    public void recieveJsonData(List<artPiece> pieces)
    {
        Debug.Log(pieces[15].title);
        for (int i = 0; i < pieces.Count; i++) 
        {
            GameObject newPiece = Instantiate(artPrefab);
            newPiece.GetComponent<artScript>().loadData(pieces[i].download, pieces[i].width, pieces[i].height);
        }
    }
}
