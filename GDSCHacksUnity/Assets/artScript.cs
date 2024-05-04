using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.Networking;
using System;
using System.IO;

public class artScript : MonoBehaviour
{


    // Start is called before the first frame update
    public void Start()
    {
        // Create a texture. Texture size does not matter, since
        // LoadImage will replace with the size of the incoming image.
         //the z is the height...not y. Data size is in cm, unit measurement is in m

    }
    public float accHeight;
    public float accWidth;


    public void loadData(string fileName, float widthCM, float heightCM)
    {
        Texture2D tex = new Texture2D(2, 2);
        byte[] imageData = File.ReadAllBytes(Application.dataPath + "/Art/Pictures/" + fileName);
        ImageConversion.LoadImage(tex, imageData);
        GetComponent<Renderer>().material.mainTexture = tex;

        accHeight = heightCM * 0.001f;
        accWidth = widthCM * 0.001f;
        transform.localScale = new Vector3(accWidth, 0.5f, accHeight);
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
