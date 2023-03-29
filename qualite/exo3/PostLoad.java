package exo3;

public class PostLoad extends Event {

	public PostLoad() {
		super("PostLoad");
	}

	public void traiter(EventInterceptor ei, Object entity){
		ei.postLoad(entity);
	}

}
