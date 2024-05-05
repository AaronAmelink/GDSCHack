using System.Collections;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using UnityEngine;

public class jsonReadWrite : MonoBehaviour
{
    // Start is called before the first frame update
    public string galleryName;
    public artHolder data;
    public gameManager gameManager;
    void loadFromJson()
    {
        string json = File.ReadAllText(Application.dataPath + "/Art/" + galleryName + "/data.json");
        data = JsonUtility.FromJson<artHolder>(json);
        gameManager.recieveJsonData(data.art, galleryName);
    }


    private void Awake()
    {
        loadFromJson();
    }
}
