using System.Collections;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using UnityEngine;

public class jsonReadWrite : MonoBehaviour
{
    // Start is called before the first frame update
    public string path = "/Art/data.json";
    public artHolder data;
    public gameManager gameManager;
    void loadFromJson()
    {
        string json = File.ReadAllText(Application.dataPath + path);
        data = JsonUtility.FromJson<artHolder>(json);
        gameManager.recieveJsonData(data.art);
    }


    private void Awake()
    {
        loadFromJson();
    }
}
