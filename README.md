# PROJECTION-OF-3D-OBJECT-SHADOW-ON-2D-PLANE-SHADOWGRAPHY

ABSTRACT:
This project is done using projective shadow concept to project 3D object’s shadow on 2D plane. So, this helps in achieving Shadowgraphy or Ombromanie in graphics programming using python

INTRODUCTION: 
Shadowgraphy or Ombromanie which is the art of performing a story or show using images made by hand shadows or gesture. Shadowgraphy is a unique art form, a combination of hands and fingers on a blank screen telling you a million stories with complete audio-visual effects. It may be called ''cinema in silhouette''. It is specifically called ''Hand Shadowgraphy''.

OBJECTIVE:
We use projective shadows technique to project shadows. This technique works by single point perspective projections with respect to XY plane. In perspective projection, the distance from the centre of projection to project plane is finite and the size of the object varies inversely with distance which looks more realistic. The distance and angles are not preserved and parallel lines do not remain parallel. Instead, they all converge at a single point called centre of projection or projection reference point. A perspective projection that forms when there exists a single principle face which is parallel to the projected plane. This is simply saying that a single vanishing point exists for an object is known as single point perspective projections.

METHODOLOGY AND MATHEMATICS:
Projective shadow projection works by using single point perspective projection technique to project shadow on XY plane that is Z=0. Consider light as a COP and light rays as projectors. Consider ZC  as centre of light with respect to Z axis.  

Here we get Final value as 
(x/(rz+1), y/(rz+1), 0, 1) as shown in figure.
Now substitute the light and each coordinates of polygon. After Substitution, plot all the new coordinates. We can able to see the shadow of the 3D object on XY Plane. 

CONCLUSION:
This technique helps shadowgraphist to visualise their hand shadows or gesture in computer using the program which is implemented in python.
